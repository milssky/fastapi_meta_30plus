import os


class ApiClient:
    def __init__(self, api_key: str, timeout: int):
        self.api_key = api_key  
        self.timeout = timeout  


class Service:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client


def main(_service: Service):
    service = _service  
    ...


if __name__ == '__main__':
    main(
        Service(
            ApiClient(
                os.getenv('API_KEY'),
                os.getenv('TIMEOUT'),
            )
        )
    )
