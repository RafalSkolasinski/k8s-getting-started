# Basic Kubernetes Deployments

This folder contains a couple of sample manifests that deploys a basic Python microservice.

## Simple Pod

The [pod.yaml](./pod.yaml) represents a simple pod.

Deploy with
```bash
$ kubectl apply -f pod.yaml
pod/microservice created
```

You can verify that pod is running with
```bash
$ kubectl get pods | grep microservice
microservice   1/1     Running   0          3m30s
```

You can enter the Pod's shell with:
```bash
$ kubectl exec -it microservice -- bash
root@microservice:/microservice#
```

Or execute commands from within the pod:
```bash
$ kubectl exec -it microservice -- curl http://localhost:8080/
```

## Basic Deployment

### Deploy

The [deployment.yaml](./deployment.yaml) contains a simple deployment and associated service.

Deploy and verify that Deployment is running
```bash
$ kubectl apply -f deployment.yaml
pod/microservice created

$ kubectl rollout status deployment/microservice
deployment "microservice" successfully rolled out

$ kubectl get pods | grep microservice
microservice-86b4b5cd67-n6xkg   1/1     Running   0          5m30s
```

### Start port-forwarding

In separate terminal start port-forwarding
```bash
$ kubectl port-forward svc/microservice 8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

### Test microservice

Now you can test the microservice
```bash
# Test root endpoint
$ curl -s http://localhost:8080/
"Hello world!"

# Test hello
$ curl -s http://localhost:8080/hello/developer

# Test secrets
$ curl -s http://localhost:8080/secrets | jq
[
  "There would be some secrets here...",
  "... but there are none."
]
```

## Config Map

The [with-config.yaml](./with-config.yaml) contains example of `Deployment` with `ConfigMap`.
`ConfigMaps` can be used to inject files and environment variables at the deployment time.

To deploy and test
```bash
# Deploy
$ kubectl apply -f with-config.yaml
configmap/microservice-config configured
deployment.apps/microservice configured
service/microservice unchanged

# Test
$ curl -s http://localhost:8080/
"Hello my dear world!"
```

## With Secret

The [with-secret.yaml](./with-secret.yaml) contains example of `Deployment` with `Secret`.
`Secrets` are usually injected by external systems in a secure way and are used to inject passwords or api tokens required on runtime, e.g. to connect to database.

To deploy and test
```bash
# Deploy
$ kubectl apply -f with-secret.yaml
secret/microservice-secret created
configmap/microservice-config configured
deployment.apps/microservice configured
service/microservice unchanged

# Test
$ curl -s http://localhost:8080/secrets | jq
[
  "This is a sample secret text.",
  "It contains multiple lines of text.",
  "Secrets should be handled with care."
]
```
