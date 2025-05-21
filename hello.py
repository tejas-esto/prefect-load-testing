from pathlib import Path
from prefect.client.schemas.schedules import CronSchedule
from prefect import flow, task

@task
def say_hello(name):
    print(f"Hello {name}!")

@flow
def hello_flow(name: str = "Marvin"):
    say_hello(name)


if __name__ == "__main__":
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    schedules = [CronSchedule(cron="15,30,45 * * * *", timezone="Europe/Tallinn")]
    hello_flow.serve(
        name=deployment_name,
        schedules=schedules,
    )