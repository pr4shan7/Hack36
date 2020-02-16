#how the frequency of routes are set
pickup_and_drop = [((data['start_station_latitude'],data['start_sattion_langitude']), (data['end_station_latitude'],data['end_station_langitude'])].map()

frequency_mapping = {}
for i in pickup_and_drop:
    if(i in frequency_mapping):
        frequency_mapping[i] += 1
    else:
        frequency_mapping[i] = 1

frequency_mapping = {k: v for k, v in sorted(frequency_mapping.items(), key=lambda item: item[1], reverse=True)}
