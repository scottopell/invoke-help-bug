"""
Example command
"""

from invoke import task

@task(help={
    "name": "unique deployment name",
    "image": "docker image name",
})
def generate(ctx,
        name,
        image="default image",
        ):
    """
    generate a deployment with the given image
    """
    print(f"Generating {name} with {image}")

