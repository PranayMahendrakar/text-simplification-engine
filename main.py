#!/usr/bin/env python3
"""Text Simplification Engine - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import VocabularySimplifier

console = Console()
simplifier = VocabularySimplifier()

def main():
    console.print(Panel("📖 TEXT SIMPLIFICATION ENGINE 📖\nMake Complex Text Accessible", style="bold blue"))
    
    while True:
        text = Prompt.ask("Complex text (or 'quit')")
        if text.lower() == 'quit': break
        level = Prompt.ask("Target level", choices=["elementary", "middle school", "high school", "general"], default="high school")
        result = simplifier.process(text, level)
        console.print(Panel(Markdown(result), title="Simplified", border_style="blue"))

if __name__ == "__main__": main()
