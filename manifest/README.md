# Manifest для запуска стэка на базе созданного приложения

Для запуска нужно:

1. Создать namespace (например через kubectl командой) под названием test-namespace:

```
kubectl create namespace test-namespace
```

2. Создать config-map для значения переменной окружения AUTHOR:

```
kubectl create configmap test-config --from-literal=author=< указать имя > 
```

3. Применить манифест:

```
kubectl apply -f webApp.yaml   
```