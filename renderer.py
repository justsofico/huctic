class Renderer:

    def show(

        self,

        exhibition,

        stats

    ):

        print(

            "\nExhibition\n"

        )

        print(

            exhibition["title"]

        )

        print()

        print(

            "Artifacts\n"

        )

        for item in exhibition["items"]:

            print(

                f"• {item.name}"

            )

        print()

        print(

            "Theme\n"

        )

        print(

            exhibition["theme"]

        )

        print()

        print(

            "Artifacts"

        )

        print(

            stats["artifacts"]

        )

        print()

        print(

            "Historical Periods"

        )

        print(

            stats["periods"]

        )
