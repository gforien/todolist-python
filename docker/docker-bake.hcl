variable ECR_SERVICES {}

target default {
    context = "."
    dockerfile = "./docker/Dockerfile"
    tags = ["${ECR_SERVICES}/todolist-service:todolist-service-python"]
}
