from ssg.site import Site
import typer


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    Site(**config).build()


