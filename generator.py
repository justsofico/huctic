import random

class Generator:

    TITLES = [

        "Machines That Changed History",

        "Across Forgotten Civilizations",

        "Inventors and Discoveries",

        "The World Before Electricity",

        "Echoes of Ancient Knowledge"

    ]

    def title(self):

        return random.choice(

            self.TITLES

        )

    def artifacts(

        self,

        items,

        count

    ):

        return random.sample(

            items,

            count

        )
