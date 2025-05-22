from pathlib import Path

from prefect import serve, flow, task
from prefect.schedules import Cron


crons_slugs = [
    ("0 * * * *", "0 min"),
    ("10 * * * *", "10 min"),
    ("20 * * * *", "20 min"),
    ("30 * * * *", "30 min"),
    ("40 * * * *", "40 min"),
    ("50 * * * *", "50 min")
]


@task
def log(cron_str: str):
    print(cron_str)

@flow(log_prints=True)
def random_flow(cron_str: str):
    log(cron_str)


if __name__ == "__main__":
    tallinn_tz = "Europe/Tallinn"
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    schedules = []
    for cron, slug in crons_slugs:
        schedules.append(
            Cron(
                cron,
                slug=slug,
                parameters={"cron_str": f"Running at {slug}"},
                timezone=tallinn_tz,
            )
        )
    random_flow.serve(
        name=deployment_name,
        schedules=schedules,
    )
