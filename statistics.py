class Statistics:

    def build(

        self,

        exhibition

    ):

        periods = {

            item.period

            for item

            in exhibition["items"]

        }

        return {

            "artifacts":

                len(

                    exhibition["items"]

                ),

            "periods":

                len(periods)

        }
