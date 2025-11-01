import os
import time
from typing import Iterator


def ft_tqdm(lst: range) -> Iterator:
    """
    Custom implementation of tqdm progress bar using yield operator.
    
    Args:
        lst: A range object to iterate over
        
    Yields:
        Each element from the range with progress bar displayed
        
    Returns:
        An iterator over the range
    """
    total = len(lst)
    start_time = time.time()
    
    # Get terminal width (default to 80 if unavailable)
    try:
        terminal_width = os.get_terminal_size().columns
    except (AttributeError, OSError):
        terminal_width = 80
    
    for i, elem in enumerate(lst, 1):
        # Calculate progress percentage
        percentage = int((i / total) * 100)
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Calculate speed (items per second)
        if elapsed_time > 0:
            speed = i / elapsed_time
        else:
            speed = float('inf')
        
        # Build progress bar
        # Format: "100%|[==========>]| 333/333 [00:01<00:00, 191.61it/s]"
        
        # Calculate bar length (leave space for other elements)
        # Percentage + brackets + numbers + time estimate needs ~60 chars
        bar_space = terminal_width - 60
        
        # If terminal is too small, use minimum bar space
        bar_space = max(20, bar_space)
        
        # Calculate filled length
        filled_length = int((i / total) * bar_space)
        
        # Build the progress bar
        # Note: at 100%, tqdm still shows > at the end
        if filled_length == bar_space:
            # 100% complete
            bar = '=' * (bar_space - 1) + '>'
        else:
            # Not complete - show progress with >
            remaining = bar_space - filled_length - 1  # -1 for the >
            bar = '=' * filled_length + '>' + ' ' * remaining
        
        # Format time
        def format_time(seconds):
            """Format seconds to MM:SS format"""
            if seconds == float('inf'):
                return "??:??"
            mins = int(seconds // 60)
            secs = int(seconds % 60)
            return f"{mins:02d}:{secs:02d}"
        
        # Calculate ETA
        if speed > 0 and speed != float('inf'):
            eta_seconds = (total - i) / speed
            eta_str = f"<{format_time(eta_seconds)}"
        else:
            eta_str = "<??:??"
        
        # Build the full progress line
        progress_line = f"{percentage}%|[{bar}]| {i}/{total} [{format_time(elapsed_time)}{eta_str}, {speed:.2f}it/s]\r"
        
        # Print progress (using \r to overwrite same line)
        print(progress_line, end='')
        
        # Yield the element
        yield elem
    
    # Print final newline
    print()


def main() -> None:
    """
    Main function to test ft_tqdm implementation.
    
    Tests the custom progress bar with a sample range to ensure
    it displays correctly and behaves like tqdm.
    """
    from time import sleep
    
    try:
        print("Testing ft_tqdm with range(50):")
        for elem in ft_tqdm(range(50)):
            sleep(0.05)
        
        print("\nTest completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
