import unittest
from pact import Consumer, Provider

class DashboardServiceContract(unittest.TestCase):

    def test_dashboard_service_contract_get(self):
        # Define the consumer and provider
        consumer = Consumer('Dashboard')
        provider = Provider('EmployeeService', host_url='http://employee-service-api')

        # Set up the interactions for HTTP GET
        consumer.has_pact_with(provider)
        pact_url = consumer.publish_pacts()

        # Verify the contract for HTTP GET
        self.assertTrue(provider.verify_pacts(pact_url))

    def test_dashboard_service_contract_post(self):
        # Define the consumer and provider
        consumer = Consumer('Dashboard')
        provider = Provider('EmployeeService', host_url='http://employee-service-api')

        # Set up the interactions for HTTP POST
        consumer.has_pact_with(provider)
        pact_url = consumer.publish_pacts()

        # Verify the contract for HTTP POST
        self.assertTrue(provider.verify_pacts(pact_url))

    def test_dashboard_service_contract_put(self):
        # Define the consumer and provider
        consumer = Consumer('Dashboard')
        provider = Provider('EmployeeService', host_url='http://employee-service-api')

        # Set up the interactions for HTTP PUT
        consumer.has_pact_with(provider)
        pact_url = consumer.publish_pacts()

        # Verify the contract for HTTP PUT
        self.assertTrue(provider.verify_pacts(pact_url))

if __name__ == '__main__':
    unittest.main()
