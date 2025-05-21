from pathlib import Path
from prefect.client.schemas.schedules import CronSchedule
from prefect import flow


@flow(log_prints=True)
def bye_flow(name: str = "Marvin"):
    print(f"Bye {name}!")


if __name__ == "__main__":
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    bye_flow.serve(
        name=deployment_name
    )