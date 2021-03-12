from data_importers.ems_importers import BaseDemocracyCountsCsvImporter


class Command(BaseDemocracyCountsCsvImporter):
    council_id = "NAY"
    addresses_name = "2021-03-02T10:36:59.539487/Democracy Club - Polling Districts.csv"
    stations_name = "2021-03-02T10:36:59.539487/Democracy Club - Polling Stations.csv"
    elections = ["2021-05-06"]

    def address_record_to_dict(self, record):
        if record.postcode == "KA30 8UA":
            return None
        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        if record.stationcode in [
            "CNS68",
            "CNS67",
            "CNS66",
            "CNS65",
            "CNS64",
            "CNS63",
            "CNS62",
            "CNS61",
            "CNS60",
            "CNS59",
            "CNS58_1",
            "CNS57_2",
            "CNS57_1",
            "CNS56",
            "CNS55",
            "CNS54",
            "CNS53",
            "CNS52",
            "CNS51",
            "CNS50",
            "CNS49",
            "CNS48",
            "CNS47",
            "CNS46",
            "CNS45",
            "CNS44",
            "CNS43_2",
            "CNS43_1",
            "CNS42",
            "CNS41_2",
            "CNS41_1",
            "CNS40",
            "CNS39_2",
            "CNS39_1",
            "CNS38",
            "CNS37",
            "CNS36",
            "CNS35",
            "CNS34",
            "CNS33",
            "CNS32_2",
            "CNS32_1",
            "CNS31",
            "CNS30",
            "CNS29",
            "CNS28",
            "CNS27",
            "CNS26",
            "CNS25_2",
            "CNS25_1",
            "CNS24",
            "CNS23",
            "CNS22",
            "CNS21",
            "CNS20",
            "CNS19",
            "CNS18",
            "CNS17",
            "CNS16",
            "CNS15",
            "CNS14",
            "CNS13",
            "CNS12",
            "CNS11",
            "CNS10_2",
            "CNS10_1",
            "CNS09",
            "CNS08_2",
            "CNS08_1",
            "CNS07",
            "CNS06",
            "CNS05_2",
            "CNS05_1",
            "CNS04",
            "CNS03_2",
            "CNS03_1",
            "CNS02",
            "CNS01",
            "CNN99",
            "CNN98",
            "CNN97",
            "CNN96",
            "CNN95",
            "CNN94",
            "CNN93",
            "CNN92_2",
            "CNN92_1",
            "CNN91",
            "CNN90",
            "CNN89",
            "CNN88",
            "CNN87",
            "CNN86",
            "CNN85",
            "CNN84",
            "CNN83_2",
            "CNN83_1",
            "CNN82",
            "CNN81",
            "CNN80",
            "CNN79_2",
            "CNN79_1",
            "CNN78",
            "CNN77",
            "CNN76",
            "CNN75",
            "CNN74",
            "CNN73",
            "CNN72",
            "CNN71",
            "CNN70",
            "CNN69",
            "CNN140",
            "CNN139",
            "CNN138",
            "CNN137",
            "CNN136",
            "CNN135",
            "CNN134",
            "CNN133",
            "CNN132",
            "CNN131",
            "CNN130",
            "CNN129",
            "CNN128",
            "CNN127",
            "CNN126",
            "CNN125",
            "CNN124",
            "CNN123",
            "CNN122",
            "CNN121",
            "CNN120",
            "CNN119",
            "CNN118",
            "CNN117",
            "CNN116",
            "CNN115",
            "CNN114_2",
            "CNN114_1",
            "CNN113",
            "CNN112",
            "CNN111",
            "CNN110",
            "CNN109",
            "CNN108",
            "CNN107",
            "CNN106_2",
            "CNN106_1",
            "CNN105_2",
            "CNN105_1",
            "CNN104",
            "CNN103_2",
            "CNN103_1",
            "CNN102_3",
            "CNN102_2",
            "CNN102_1",
            "CNN101",
            "CNN100",
        ]:
            return super().station_record_to_dict(record)
        else:
            return None
