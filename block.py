from pathlib import Path
from prefect.client.schemas.schedules import CronSchedule
from prefect.blocks.system import Secret
from prefect import flow, task

@task
def print_secret():
    random_secret = Secret.load("random-secret-string").get()
    print(random_secret)

@flow(log_prints=True)
def blocks_flow():
    print_secret()


if __name__ == "__main__":
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    schedules = [CronSchedule(cron="30 * * * *", timezone="Europe/Tallinn")]
    blocks_flow.serve(
        name=deployment_name,
        schedules=schedules,
    )
