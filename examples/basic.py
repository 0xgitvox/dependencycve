"""Minimal example for DependencyCVE."""

from dependencycve import dependencycve


def main():
 runner = dependencycve({"name": "DependencyCVE", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()