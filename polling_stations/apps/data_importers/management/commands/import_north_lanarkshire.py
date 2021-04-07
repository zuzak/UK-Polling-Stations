from data_importers.ems_importers import BaseHalaroseCsvImporter

SLK_EXCLUDE_STATIONS = (
    "3-eastfield-community-centre",
    "3-st-nicholas-parish-church-hall",
    "1-long-calderwood-primary-school",
    "3-law-primary-school",
    "1-st-marks-primary-school",
    "1-west-coats-primary-school",
    "2-east-kilbride-old-parish-church-hall",
    "1-east-milton-primary-school",
    "5-mossneuk-primary-school",
    "1-st-blanes-primary-school",
    "5-south-lanarkshire-lifestyles-carluke",
    "4-wester-overton-primary-school",
    "1-coulter-hall",
    "1-eddlewood-public-hall",
    "1-crawforddyke-primary-school",
    "1-claremont-parish-church-hall",
    "2-calderwood-primary-school",
    "1-springhall-community-centre",
    "3-south-lanarkshire-lifestyles-fairhill",
    "1-high-blantyre-primary-school",
    "4-blackwood-primary-school",
    "4-st-charles-primary-school",
    "1-st-leonards-primary-school",
    "4-whitehill-neighbourhood-centre",
    "1-kirkfieldbank-hall",
    "3-glengowan-primary-school",
    "1-calderwood-primary-school",
    "1-south-park-primary-school",
    "1-park-church",
    "5-st-kenneths-primary-school",
    "2-kirkton-primary-school",
    "3-david-milne-centre",
    "1-blacklaw-primary-school",
    "5-hillhouse-and-earnock-community-centre",
    "1-thankerton-hall",
    "1-woodhead-primary-school",
    "4-mossneuk-primary-school",
    "3-hallside-primary-school",
    "2-springhall-community-centre",
    "4-tact-community-hall",
    "3-eddlewood-public-hall",
    "1-kirkton-primary-school",
    "2-rutherglen-united-reformed-church-hall",
    "1-calderwood-hall",
    "2-ballerup-recreation-area-pavilion",
    "2-st-vincents-primary-school",
    "1-leadhills-hall",
    "2-st-kenneths-primary-school",
    "4-crawforddyke-primary-school",
    "2-udston-primary-school",
    "3-machanhill-primary-school",
    "3-calderwood-primary-school",
    "1-pettinain-hall",
    "1-hillhouse-and-earnock-community-centre",
    "3-craigbank-primary-school-community-wing-entrance",
    "7-st-kenneths-primary-school",
    "1-rutherglen-west-and-wardlawhill-parish-church-hall",
    "2-carstairs-community-centre",
    "3-blackwood-primary-school",
    "1-robert-owen-memorial-primary-school",
    "4-stonehouse-primary-school",
    "2-woodhead-primary-school",
    "1-braehead-hall",
    "1-rigside-community-hall",
    "1-biggar-municipal-hall",
    "4-townhill-primary-school",
    "4-whitlawburn-community-resource-centre",
    "2-machanhill-primary-school",
    "2-south-lanarkshire-lifestyles-carluke",
    "3-fernhill-community-centre",
    "1-glengowan-primary-school",
    "1-mossneuk-primary-school",
    "3-uddingston-community-centre",
    "3-wester-overton-primary-school",
    "1-bothwell-primary-school",
    "1-st-charles-primary-school",
    "1-mount-cameron-primary-school",
    "1-kirktonholme-primary-school",
    "2-murray-primary-school",
    "2-st-marys-clubrooms",
    "1-wester-overton-primary-school",
    "2-south-lanarkshire-lifestyles-fairhill",
    "1-avendale-old-parish-church-hall",
    "1-crawford-hall",
    "1-auchenheath-hall",
    "2-whitlawburn-community-resource-centre",
    "1-south-lanarkshire-council-offices",
    "1-springwells-neighbourhood-hall",
    "2-flemington-hallside-church-hall",
    "3-north-halfway-community-hall",
    "3-long-calderwood-primary-school",
    "2-hamilton-caledonian-bowling-club",
    "1-symington-hall",
    "2-eddlewood-public-hall",
    "2-halfmerke-primarywest-mains-school",
    "1-st-josephs-primary-school-nursery-entrance",
    "2-st-elizabeths-primary-school-side-entrance",
    "3-st-charles-primary-school",
    "2-st-brides-centre",
    "1-hamilton-caledonian-bowling-club",
    "2-chatelherault-primary-school",
    "2-st-josephs-primary-school-nursery-entrance",
    "4-crosshouse-primary-school",
    "1-new-lanark-primary-school",
    "1-chatelherault-primary-school",
    "2-springwells-neighbourhood-hall",
    "4-hallside-primary-school",
    "2-cairns-primary-school",
    "6-st-kenneths-primary-school",
    "1-craigbank-primary-school-community-wing-entrance",
    "1-the-fountain",
    "3-canberra-primary-school",
    "1-quarter-primary-school",
    "2-mossneuk-parish-church",
    "1-our-lady-and-st-annes-primary-school",
    "1-dalserf-parish-church-hall",
    "1-brocketsbrae-hall",
    "1-whitlawburn-community-resource-centre",
    "2-our-lady-and-st-annes-primary-school",
    "1-elsrickle-hall",
    "2-hunter-primary-school",
    "2-st-peters-primary-school",
    "1-hareleeshill-primary-school-community-wing-entrance",
    "1-trinity-parish-church-hall",
    "1-maxwellton-primary-schoolgreenburn-school",
    "5-stonehouse-primary-school",
    "1-roberton-public-hall",
    "2-wester-overton-primary-school",
    "2-uddingston-community-centre",
    "2-auchinraith-primary-school",
    "1-quothquan-hall",
    "1-st-marys-clubrooms",
    "2-st-johns-primary-school",
    "1-burnside-blairbeth-parish-church-hall",
    "2-hillhouse-and-earnock-community-centre",
    "2-east-milton-primary-school",
    "2-high-blantyre-primary-school",
    "2-trinity-parish-church-hall",
    "3-trinity-parish-church-hall",
    "2-glengowan-primary-school",
    "2-hallside-primary-school",
    "3-east-milton-primary-school",
    "3-bankhead-primary-school",
    "2-st-charles-primary-school",
    "1-woodpark-primary-school",
    "1-greenhills-primary-school",
    "1-nemphlar-hall",
    "4-bankhead-primary-school",
    "1-law-primary-school",
    "3-our-lady-and-st-annes-primary-school",
    "2-eastfield-community-centre",
    "2-biggar-municipal-hall",
    "3-blacklaw-primary-school",
    "2-heatheryknowe-primary-school",
    "1-burgh-primary-school",
    "1-crossford-hall",
    "3-maxwellton-primary-schoolgreenburn-school",
    "2-glenlee-primary-school",
    "1-st-vincents-primary-school",
    "4-udston-primary-school",
    "1-alistair-mccoist-complex",
    "2-long-calderwood-primary-school",
    "1-hallside-primary-school",
    "4-st-kenneths-primary-school",
    "1-carstairs-junction-hall",
    "1-glenlee-primary-school",
    "1-stonehouse-primary-school",
    "1-south-lanarkshire-lifestyles-carluke",
    "1-braidwood-primary-school",
    "3-forth-primary-school",
    "3-st-kenneths-primary-school",
    "2-mount-cameron-primary-school",
    "1-tact-community-hall",
    "3-crosshouse-primary-school",
    "1-woodside-primary-school",
    "1-carmichael-hall",
    "2-claremont-parish-church-hall",
    "2-north-halfway-community-hall",
    "2-tact-community-hall",
    "1-st-brides-primary-school",
    "1-blackwood-primary-school",
    "3-townhill-primary-school",
    "1-stewartfield-community-centre",
    "1-uddingston-community-centre",
    "1-auchinraith-primary-school",
    "3-st-leonards-primary-school",
    "4-hillhouse-and-earnock-community-centre",
    "2-blacklaw-primary-school",
    "1-rutherglen-united-reformed-church-hall",
    "2-burgh-primary-school",
    "3-crawforddyke-primary-school",
    "1-high-blantyre-public-hall",
    "2-craigbank-primary-school-community-wing-entrance",
    "1-crosshouse-primary-school",
    "2-whitehill-neighbourhood-centre",
    "2-south-park-primary-school",
    "3-west-coats-primary-school",
    "1-bothwell-community-hall",
    "3-rutherglen-united-reformed-church-hall",
    "3-south-lanarkshire-lifestyles-carluke",
    "1-universal-connections",
    "2-spittal-primary-school",
    "3-hillhouse-and-earnock-community-centre",
    "1-tarbrax-village-hall",
    "1-cathkin-primary-school-community-wing",
    "5-crawforddyke-primary-school",
    "2-robert-owen-memorial-primary-school",
    "1-east-kilbride-old-parish-church-hall",
    "1-st-nicholas-parish-church-hall",
    "2-st-brides-primary-school-nursery-entrance",
    "1-auchengray-primary-school",
    "1-carstairs-community-centre",
    "2-stonehouse-primary-school",
    "3-whitlawburn-community-resource-centre",
    "2-bankhead-primary-school",
    "3-hunter-primary-school",
    "3-biggar-municipal-hall",
    "3-high-blantyre-public-hall",
    "2-ferniegair-community-hall",
    "3-kirkton-primary-school",
    "1-sandford-primary-school",
    "1-north-halfway-community-hall",
    "2-townhill-primary-school",
    "2-greenhills-primary-school",
    "3-bothwell-community-hall",
    "2-east-mains-united-reformed-church-hall",
    "2-high-blantyre-public-hall",
    "1-forth-primary-school",
    "2-st-blanes-primary-school",
    "1-heatheryknowe-primary-school",
    "1-machanhill-primary-school",
    "1-spittal-primary-school",
    "2-woodside-primary-school",
    "1-david-milne-centre",
    "1-auldhouse-primary-school",
    "1-cairns-primary-school",
    "2-st-nicholas-parish-church-hall",
    "1-flemington-hallside-church-hall",
    "2-dalserf-primary-school-community-wing",
    "2-law-primary-school",
    "2-st-leonards-primary-school",
    "1-greenhills-hall",
    "1-st-johns-primary-school",
    "2-james-aiton-primary-school",
    "5-udston-primary-school",
    "2-rutherglen-west-and-wardlawhill-east-church-hall",
    "1-dolphinton-hall",
    "2-stewartfield-community-centre",
    "3-st-peters-primary-school",
    "1-st-brides-centre",
    "1-whitehill-neighbourhood-centre",
    "4-long-calderwood-primary-school",
    "2-kirklandpark-primary-school",
    "3-tact-community-hall",
    "2-canberra-primary-school",
    "2-greenhills-hall",
    "2-crawforddyke-primary-school",
    "3-murray-primary-school",
    "2-mossneuk-primary-school",
    "2-st-brides-primary-school",
    "2-bothwell-community-hall",
    "3-st-johns-primary-school",
    "1-halfmerke-primarywest-mains-school",
    "2-st-marks-primary-school",
    "4-murray-primary-school",
    "5-bankhead-primary-school",
    "2-forth-primary-school",
    "3-whitehill-neighbourhood-centre",
    "3-st-vincents-primary-school",
    "1-kirklandpark-primary-school",
    "2-woodpark-primary-school",
    "1-glespin-community-hall",
    "1-townhill-primary-school",
    "2-bothwell-primary-school",
    "2-david-milne-centre",
    "1-dalserf-primary-school-community-wing",
    "1-caledonian-centre",
    "3-mossneuk-primary-school",
    "1-lanark-primary-school",
    "2-alistair-mccoist-complex",
    "2-the-fountain",
    "2-coalburn-leisure-complex",
    "1-mossneuk-parish-church",
    "1-st-hilarys-primary-school",
    "3-woodhead-primary-school",
    "2-lanark-primary-school",
    "1-castlefield-primary-school",
    "1-st-peters-primary-school",
    "3-stonehouse-primary-school",
    "3-st-elizabeths-primary-school-side-entrance",
    "4-south-lanarkshire-lifestyles-carluke",
    "1-st-brides-primary-school-nursery-entrance",
    "2-castlefield-primary-school",
    "1-james-aiton-primary-school",
    "1-abington-hall",
    "1-ferniegair-community-hall",
    "3-stewartfield-community-centre",
    "1-east-mains-united-reformed-church-hall",
    "1-glassford-primary-school",
    "2-blackwood-primary-school",
    "4-west-coats-primary-school",
    "1-gilmourton-primary-school",
    "2-avendale-old-parish-church-hall",
    "1-udston-primary-school",
    "2-maxwellton-primary-schoolgreenburn-school",
    "5-st-charles-primary-school",
    "1-ballerup-recreation-area-pavilion",
    "3-kirklandpark-primary-school",
    "1-thorntonhall-lawn-tennis-club",
    "1-carnwath-primary-school",
    "1-rutherglen-west-and-wardlawhill-east-church-hall",
    "2-park-church",
    "1-canberra-primary-school",
    "2-crosshouse-primary-school",
    "2-fernhill-community-centre",
    "1-chapelton-primary-school",
    "1-eastfield-community-centre",
    "1-bankhead-primary-school",
    "2-west-coats-primary-school",
    "1-fernhill-community-centre",
    "1-murray-primary-school",
    "1-south-lanarkshire-lifestyles-fairhill",
    "2-cathkin-primary-school-community-wing",
    "1-st-kenneths-primary-school",
    "1-hunter-primary-school",
    "1-st-elizabeths-primary-school-side-entrance",
    "3-st-blanes-primary-school",
    "1-netherburn-community-hall",
    "3-chatelherault-primary-school",
    "2-carnwath-primary-school",
    "2-hareleeshill-primary-school-community-wing-entrance",
    "3-rutherglen-west-and-wardlawhill-east-church-hall",
    "3-lanark-primary-school",
    "1-coalburn-leisure-complex",
    "3-udston-primary-school",
    "3-glenlee-primary-school",
    "3-hareleeshill-primary-school-community-wing-entrance",
)


class Command(BaseHalaroseCsvImporter):
    council_id = "NLK"
    addresses_name = "2021-04-06T11:57:09.061900/North and South Lanarkshire polling_station_export-2021-04-02.csv"
    stations_name = "2021-04-06T11:57:09.061900/North and South Lanarkshire polling_station_export-2021-04-02.csv"
    elections = ["2021-05-06"]

    def address_record_to_dict(self, record):
        station_hash = self.get_station_hash(record)
        if station_hash in SLK_EXCLUDE_STATIONS:
            return None
        if record.housepostcode in [
            "ML2 9NG",
            "ML6 7SE",
            "ML6 9BA",
            "ML6 8QN",
            "ML6 8HQ",
            "ML6 8LW",
            "ML5 5QH",
            "G69 9JF",
            "G69 8AA",
            "G69 8BW",
            "G67 2AG",
            "G68 0AN",
            "G68 9DB",
            "G65 9NG",
            "ML4 2RE",
            "ML1 4TU",
            "ML4 1RF",
            "ML1 2TD",
            "ML1 2BP",
            "ML2 0DG",
        ]:
            return None
        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        station_hash = self.get_station_hash(record)
        if station_hash in SLK_EXCLUDE_STATIONS:
            return None

        if station_hash in [
            "1-st-marys-primary-school",
            "1-community-education-centre",
            "1-masonic-hall",
            "2-masonic-hall",
        ]:
            return None
        return super().station_record_to_dict(record)
