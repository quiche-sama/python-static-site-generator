from ssg.site import Site
import typer


def main(source="content", dest="dist"):
    config = {"config": source, "dest": dest}
