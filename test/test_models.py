from src.models.restaurants import read_csv
import tempfile


class TestRestaurantsModel:

    def test_read_csv(
        self,
        csv_file_content,
        create_restaurant
    ):
        r1 = [create_restaurant()]
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_csv:
            temp_csv.write(csv_file_content)
            temp_csv_path = temp_csv.name

        try:
            restaurants = read_csv(temp_csv_path)
            assert restaurants == r1
        finally:
            import os
            os.remove(temp_csv_path)
