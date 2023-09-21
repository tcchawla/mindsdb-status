import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name


class TestMediaWikiConnection(BaseTest):
    """
    Test class for testing the MediaWiki datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new MediaWiki Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("mediawiki_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "mediawiki",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Media Wiki", "clmt4gm0n12728b8n3e6nkz55p")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
