"""Main entry point for running evaluations."""
import kimera_eval.tools.evaluate
import kimera_eval.tools.run
import kimera_eval.tools.summary
import kimera_eval.tools.timing
import kimera_eval.tools.website
import kimera_eval.website

from kimera_eval.logger import configure_logging

import click


@click.group()
@click.option("-l", "--log-level", default="INFO", help="log level")
def main(log_level):
    """Command-line tool to evaluate Kimera-VIO."""
    configure_logging(level=log_level)


main.add_command(kimera_eval.tools.run.run)
main.add_command(kimera_eval.tools.evaluate.run)
main.add_command(kimera_eval.tools.timing.run)
main.add_command(kimera_eval.tools.summary.run)
main.add_command(kimera_eval.tools.website.run)


if __name__ == "__main__":
    main()