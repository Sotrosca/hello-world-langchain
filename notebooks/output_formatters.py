def _print_separator(char="=", width=80):
    """Print a separator line."""
    print(char * width)


def _print_header(title, width=80):
    """Print a header with title."""
    _print_separator("=", width)
    print(title)
    _print_separator("=", width)


def _print_step_header(step_num, node_name, width=80):
    """Print a step header."""
    print(f"\n{'─' * width}")
    print(f"Step {step_num}: {node_name.upper()}")
    print("─" * width)


def _wrap_text(text, indent="  ", max_width=78):
    """
    Wrap text to fit within max_width with proper indentation.

    Args:
        text: Text to wrap
        indent: String to prepend to each line
        max_width: Maximum line width including indent
    """
    words = text.split()
    line = indent

    for word in words:
        if len(line) + len(word) + 1 > max_width:
            print(line)
            line = indent + word
        else:
            line += (" " if line != indent else "") + word

    if line.strip():
        print(line)


def _print_content_truncated(content, max_length=500, indent="  "):
    """Print content with truncation if too long."""
    if len(content) > max_length:
        print(f"{indent}{content[:max_length]}...")
        print(f"\n{indent}[Content truncated - {len(content)} chars total]")
    else:
        _wrap_text(content, indent=indent)


def _print_metadata(msg):
    """Print message metadata if available."""
    if not hasattr(msg, "response_metadata") or not msg.response_metadata:
        return

    metadata = msg.response_metadata
    print(f"\n  Metadata:")

    if "model" in metadata:
        print(f"    Model: {metadata['model']}")

    if "total_duration" in metadata:
        duration_sec = metadata["total_duration"] / 1e9
        print(f"    Duration: {duration_sec:.2f}s")

    if hasattr(msg, "usage_metadata") and msg.usage_metadata:
        usage = msg.usage_metadata
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        print(f"    Tokens: {input_tokens} in / {output_tokens} out")


def _print_message_detailed(msg, msg_idx):
    """Print a single message with full details."""
    msg_type = type(msg).__name__
    print(f"\n  Message {msg_idx} [{msg_type}]:")
    print(f"  {'-' * 76}")

    _print_content_truncated(msg.content)
    _print_metadata(msg)


def _print_message_summary(msg):
    """Print a single message in summary format."""
    msg_type = type(msg).__name__
    print(f"\n  [{msg_type}]")
    print(f"  {msg.content}\n")


def _process_messages(messages, detailed=True):
    """
    Process and print messages.

    Args:
        messages: List of messages to process
        detailed: If True, show detailed output; if False, show summary
    """
    if detailed:
        for msg_idx, msg in enumerate(messages, 1):
            _print_message_detailed(msg, msg_idx)
    else:
        for msg in messages:
            _print_message_summary(msg)


def _process_graph_steps(calls, detailed=True):
    """
    Process and print graph execution steps.

    Args:
        calls: List of dictionaries from graph.stream()
        detailed: If True, show detailed output; if False, show summary
    """
    for idx, step in enumerate(calls, 1):
        for node_name, data in step.items():
            _print_step_header(idx, node_name)

            if "messages" in data:
                _process_messages(data["messages"], detailed=detailed)


def format_graph_output(calls):
    """
    Format LangGraph output in a human-readable way with full details.

    Args:
        calls: List of dictionaries from graph.stream()
    """
    _print_header("GRAPH EXECUTION SUMMARY")
    _process_graph_steps(calls, detailed=True)

    print(f"\n{'=' * 80}")
    print(f"Total steps: {len(calls)}")
    _print_separator("=")


def format_graph_output_summary(calls):
    """
    Format LangGraph output in a summarized way - shows only step, message type, and full content.

    Args:
        calls: List of dictionaries from graph.stream()
    """
    _print_header("GRAPH EXECUTION SUMMARY (Condensed)")
    _process_graph_steps(calls, detailed=False)

    print(f"{'=' * 80}")
    print(f"Total steps: {len(calls)}")
    _print_separator("=")
