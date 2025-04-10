"""
Profiling utilities for the Æther project.
"""

import functools
import time
import tracemalloc
from typing import Any, Callable, Dict, List, Tuple, TypeVar, cast

from aether.utils.logging import get_logger

logger = get_logger(__name__)

# Type variable for generic function
F = TypeVar("F", bound=Callable[..., Any])


def timeit(func: F) -> F:
    """
    Decorator to measure the execution time of a function.

    Args:
        func: The function to be timed.

    Returns:
        Wrapped function that logs execution time.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        logger.debug(
            f"{func.__name__} took {end_time - start_time:.4f} seconds to execute"
        )

        return result

    return cast(F, wrapper)


def memory_usage(func: F) -> F:
    """
    Decorator to measure the memory usage of a function.

    Args:
        func: The function whose memory usage will be measured.

    Returns:
        Wrapped function that logs memory usage.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        tracemalloc.start()

        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()
        logger.debug(
            f"{func.__name__} used {current / 1024:.2f} KB current, {peak / 1024:.2f} KB peak"
        )

        return result

    return cast(F, wrapper)


class Timer:
    """
    Context manager for timing code blocks.

    Example:
        with Timer("Processing files") as timer:
            process_files()
    """

    def __init__(self, name: str):
        """
        Initialize the timer.

        Args:
            name: Name of the code block being timed.
        """

        self.name = name
        self.start_time = 0.0
        self.end_time = 0.0

    def __enter__(self) -> "Timer":
        """
        Start timing when entering the context.

        Returns:
            The Timer instance.
        """

        self.start_time = time.time()
        return self

    def __exit__(self, *args: Any) -> None:
        """
        Stop timing when exiting the context and log the elapsed time.
        """

        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        logger.debug(f"{self.name} took {elapsed:.4f} seconds")


class MemoryTracker:
    """
    Context manager for tracking memory usage.

    Example:
        with MemoryTracker("Large data processing") as tracker:
            process_large_data()
    """

    def __init__(self, name: str):
        """
        Initialize the memory tracker.

        Args:
            name: Name of the code block being tracked.
        """

        self.name = name

    def __enter__(self) -> "MemoryTracker":
        """
        Start tracking memory when entering the context.

        Returns:
            The MemoryTracker instance.
        """

        tracemalloc.start()
        return self

    def __exit__(self, *args: Any) -> None:
        """
        Stop tracking memory when exiting the context and log the usage.
        """

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        logger.debug(
            f"{self.name} memory usage: {current / 1024:.2f} KB current, "
            f"{peak / 1024:.2f} KB peak"
        )


class PerformanceStats:
    """
    Collect and report performance statistics.
    """

    def __init__(self):
        """Initialize the performance stats collector."""
        self.function_times: Dict[str, List[float]] = {}
        self.function_memory: Dict[str, List[Tuple[int, int]]] = {}

    def add_time(self, function_name: str, elapsed_time: float) -> None:
        """
        Add a timing measurement for a function.

        Args:
            function_name: Name of the function.
            elapsed_time: Time taken in seconds.
        """
        if function_name not in self.function_times:
            self.function_times[function_name] = []

        self.function_times[function_name].append(elapsed_time)

    def add_memory_usage(self, function_name: str, current: int, peak: int) -> None:
        """
        Add a memory usage measurement for a function.

        Args:
            function_name: Name of the function.
            current: Current memory usage in bytes.
            peak: Peak memory usage in bytes.
        """
        if function_name not in self.function_memory:
            self.function_memory[function_name] = []

        self.function_memory[function_name].append((current, peak))

    def get_timing_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get timing statistics for all measured functions.

        Returns:
            Dictionary mapping function names to timing statistics.
        """

        stats = {}

        for func_name, times in self.function_times.items():
            if not times:
                continue

            stats[func_name] = {
                "count": len(times),
                "total": sum(times),
                "average": sum(times) / len(times),
                "min": min(times),
                "max": max(times),
            }

        return stats

    def get_memory_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get memory usage statistics for all measured functions.

        Returns:
            Dictionary mapping function names to memory statistics.
        """

        stats = {}
        for func_name, usages in self.function_memory.items():
            if not usages:
                continue

            current_values = [current for current, _ in usages]
            peak_values = [peak for _, peak in usages]

            stats[func_name] = {
                "count": len(usages),
                "avg_current": sum(current_values) / len(current_values) / 1024,  # KB
                "avg_peak": sum(peak_values) / len(peak_values) / 1024,  # KB
                "max_peak": max(peak_values) / 1024,  # KB
            }

        return stats

    def report(self) -> str:
        """
        Generate a performance report.

        Returns:
            A formatted string containing performance statistics.
        """

        timing_stats = self.get_timing_stats()
        memory_stats = self.get_memory_stats()

        lines = ["Performance Report", "=================", ""]

        # Timing statistics
        if timing_stats:
            lines.append("Timing Statistics:")
            lines.append("-----------------")

            for func_name, stats in sorted(timing_stats.items()):
                lines.append(f"Function: {func_name}")
                lines.append(f"  Calls:   {stats['count']}")
                lines.append(f"  Total:   {stats['total']:.4f} sec")
                lines.append(f"  Average: {stats['average']:.4f} sec")
                lines.append(f"  Min:     {stats['min']:.4f} sec")
                lines.append(f"  Max:     {stats['max']:.4f} sec")
                lines.append("")

        # Memory statistics
        if memory_stats:
            lines.append("Memory Statistics:")
            lines.append("-----------------")

            for func_name, stats in sorted(memory_stats.items()):
                lines.append(f"Function: {func_name}")
                lines.append(f"  Measurements: {stats['count']}")
                lines.append(f"  Avg Current:  {stats['avg_current']:.2f} KB")
                lines.append(f"  Avg Peak:     {stats['avg_peak']:.2f} KB")
                lines.append(f"  Max Peak:     {stats['max_peak']:.2f} KB")
                lines.append("")

        return "\n".join(lines)

    def log_report(self) -> None:
        """Log the performance report."""
        logger.info(self.report())


performance_stats = PerformanceStats()


def track_performance(func: F) -> F:
    """
    Decorator to track both time and memory performance of a function.

    Args:
        func: The function to track.

    Returns:
        Wrapped function that tracks performance.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        tracemalloc.start()

        try:
            result = func(*args, **kwargs)

            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()

            elapsed = end_time - start_time
            performance_stats.add_time(func.__name__, elapsed)
            performance_stats.add_memory_usage(func.__name__, current, peak)

            return result

        finally:
            tracemalloc.stop()

    return cast(F, wrapper)
