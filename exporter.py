class Exporter:

    def save(

        self,

        exhibition,

        filename="catalog.txt"

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                exhibition["title"]

            )

            file.write("\n\n")

            for artifact in exhibition["items"]:

                file.write(

                    f"- {artifact.name}\n"

                )
