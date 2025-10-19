from datetime import datetime

# Get current time
now = datetime.now()

# Calculate seconds since January 1, 1970 (Unix epoch)
seconds_since_epoch = now.timestamp()

# Format seconds with comma separator
formatted_seconds = f"{seconds_since_epoch:,.4f}"

# Format in scientific notation
scientific_notation = f"{seconds_since_epoch:.2e}"

# Format date as "Oct 21 2022"
formatted_date = now.strftime("%b %d %Y")

# Print the output
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(formatted_date)

