# Obsidian Notes MCP Server

**Facilitating integration between Large Language Models and local Knowledge Bases.**

The Obsidian Notes Model Context Protocol (MCP) server provides a standardized interface for AI models (such as those utilized in LM Studio, Claude Desktop, and other MCP-compatible clients) to interact with a local **Obsidian Vault**. This implementation enables AI agents to navigate directory structures, index available notes, and retrieve Markdown content in real-time, effectively extending the model's context with personal knowledge.

---

## Key Capabilities

*   **Recursive Vault Indexing:** Provides a comprehensive list of all Markdown files and directories within the vault, automatically excluding system directories (e.g., `.git`, `.obsidian`).
*   **Contextual Content Retrieval:** Facilitates the retrieval of full Markdown note content for use as grounding context in LLM prompts.
*   **Enhanced Security:** Implements robust path validation and traversal protection to ensure access is restricted to the designated vault directory.
*   **Standards-Compliant:** Developed using the `fastmcp` SDK, ensuring compatibility with the Model Context Protocol.

---

## Technical Prerequisites

*   **Python 3.10 or higher**
*   An **Obsidian Vault** or a structured directory of Markdown files.
*   An **MCP-compatible Client** (e.g., LM Studio, Claude Desktop, or MCP Inspector).

---

## Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd obsidian-notes-server
    ```

2.  **Environment Setup:**
    It is recommended to use a virtual environment for dependency management.
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

    pip install -r requirements.txt
    ```

---

## Configuration

The server requires the absolute path to your Obsidian Vault.

1.  Open `server.py`.
2.  Modify the `VAULT_PATH` variable:
    ```python
    # Specify the absolute path to your vault
    VAULT_PATH = r"C:\Path\To\Your\Obsidian Vault"
    ```
3.  Save the modifications.

---

## Usage and Integration

### Server Verification
To verify the server executes correctly within your environment:
```bash
python server.py
```
*Note: While MCP servers are typically invoked by client applications, manual execution confirms the environment is correctly configured.*

### Client Integration (e.g., LM Studio)


Incorporate the following configuration into your MCP client settings:

```json
{
  "mcpServers": {
    "obsidian-notes-server": {
      "command": "C:/path/to/your/venv/Scripts/python.exe",
      "args": [
        "C:/path/to/your/repo/server.py"
      ]
    }
  }
}
```

For detailed guidance on integrating MCP servers with LM Studio, please refer to the [official documentation](https://lmstudio.ai/docs/app/mcp).

---

## Tool Documentation

### `list_notes()`
Recursively retrieves all Markdown file paths within the vault.
*   **Returns:** A newline-delimited string of relative file paths.

### `list_folders()`
Retrieves all directory paths within the vault to provide structural context.
*   **Returns:** A newline-delimited string of relative folder paths.

### `read_note(filename: str)`
Retrieves the raw text content of a specified note.
*   **Parameters:**
    *   `filename`: The relative path to the Markdown file.
*   **Returns:** The complete string content of the document.
*   **Exception Handling:** Returns sanitized error messages in the event of missing files or security violations.

---

## Security Architecture

*   **Read-Only Access:** The server is restricted to read operations. It does not possess the capability to modify, delete, or create files within the vault.
*   **Input Validation:** The `read_note` tool implements strict input sanitization, rejecting any paths containing parent directory references (`..`) or absolute path indicators to prevent directory traversal attacks.

---

## Further Information

For a detailed breakdown and comprehensive information regarding the Obsidian Notes MCP Server, please visit:
[project-breakdown101.web.app](https://project-breakdown101.web.app/)