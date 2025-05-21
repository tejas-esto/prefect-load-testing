from pathlib import Path
from prefect.client.schemas.schedules import CronSchedule
from prefect import flow


@flow
def hello_flow(name: str = "Marvin"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    schedules = [CronSchedule(cron="30 * * * *", timezone="Europe/Tallinn")]
    hello_flow.serve(
        name=deployment_name,
        schedules=schedules,
    )