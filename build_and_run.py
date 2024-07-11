import subprocess

def build_docker_image():
    subprocess.run(["docker", "build", "-t", "app", "."])

def run_docker_container():
    subprocess.run(["docker", "run", "-p", "5000:5000", "app"])

if __name__ == "__main__":
    build_docker_image()
    run_docker_container()
