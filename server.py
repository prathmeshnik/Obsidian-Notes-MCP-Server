from fastmcp import FastMCP
import os

# Initialize the server
mcp = FastMCP("obsidian-notes-server")

VAULT_PATH = r"C:\Path\To\Your\Obsidian Vault" 

@mcp.tool()
def list_notes() -> str:
    """Lists all markdown files in the vault."""
    try:
        notes = []
        for root, dirs, files in os.walk(VAULT_PATH):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for filename in files:
                if filename.endswith(".md"):
                    full_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(full_path, VAULT_PATH)
                    notes.append(rel_path.replace("\\", "/"))
        return "\n".join(notes)
    except Exception as e:
        return f"Error accessing vault: {str(e)}"

@mcp.tool()
def list_folders() -> str:
    """Lists all folders and subfolders in the vault, excluding hidden ones."""
    try:
        folders = []
        for root, dirs, files in os.walk(VAULT_PATH):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for d in dirs:
                full_path = os.path.join(root, d)
                rel_path = os.path.relpath(full_path, VAULT_PATH)
                folders.append(rel_path.replace("\\", "/"))
                
        return "\n".join(folders)
    except Exception as e:
        return f"Error listing folders: {str(e)}"

@mcp.tool()
def read_note(filename: str) -> str:
    """Reads the content of a specific note from the vault."""
    filename = os.path.normpath(filename)
    if ".." in filename or filename.startswith(os.sep):
        return "Error: Invalid filename."
    
    full_path = os.path.join(VAULT_PATH, filename)
    
    if not os.path.exists(full_path):
        return f"Error: File not found at {full_path}"
        
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

if __name__ == "__main__":
    mcp.run()