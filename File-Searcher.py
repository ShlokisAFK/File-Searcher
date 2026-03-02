import os
from rich import print
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

Console=Console()
def search(file):
    arr=[]
    with Progress(SpinnerColumn(), TextColumn("{task.description}")) as progress:
        task = progress.add_task("Searching ...", total=None)
        for root,dir,files in os.walk("D://"):
            progress.update(task ,description=f"Searching: {root[:40]} ")
            for f in files:
                if(file.lower() in f.lower()):
                    print(f"[cyan]Directory: [/cyan] {root} | [green]File : [/green] {f}")
                    arr.append(root)
    if len(arr) == 0:
        print("404")
file=input("Enter file name : ")
search(file)