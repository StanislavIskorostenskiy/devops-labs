# devops-labs
my study DevOps pet

docker build -t xmaoax/devops-labs:latest .
docker push xmaoax/devops-labs:latest

kubectl apply -f k8s/deployment.yaml
kubectl rollout restart deployment fastapi-app

kubectl logs -f deployment/fastapi-app

kubectl --kubeconfig=.kubeconfig.yml apply -f k8s/deployment.yml
kubectl --kubeconfig=.kubeconfig.yml apply -f k8s/service.yml
kubectl --kubeconfig=.kubeconfig.yml get svc postgres
kubectl --kubeconfig=.kubeconfig.yml get pods
kubectl --kubeconfig=.kubeconfig.yml logs


┌───────────────┐        ┌──────────────────┐
│               │        │                  │
│ Внешний мир   │ <----> │ devopslab-service │  <- LoadBalancer, внешний IP
│ (пользователи)│        │ (порт 80)         │
└───────────────┘        └─────────┬────────┘
                                    │ направляет трафик на
                            ┌───────▼──────────┐
                            │ devopslab-под    │
                            │ (приложение)     │
                            │ порт 8000        │
                            └───────┬──────────┘
                                    │ подключается к базе по DNS-имени "postgres"
                           ┌────────▼───────────┐
                           │ postgres-сервис    │
                           │ (порт 5432)        │
                           └────────┬───────────┘
                                    │ направляет запросы на
                           ┌────────▼───────────┐
                           │ postgres-под       │
                           │ (база данных)      │
                           │ порт 5432          │
                           └────────────────────┘