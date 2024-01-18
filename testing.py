def test_traffic_model():
    mas_response_times = []
    mas_congestion_occurrences = []
    baseline_response_times = []
    baseline_congestion_occurrences = []

    for _ in range(10):  
        mas_response_time, mas_congestion = run_model('MAS')
        baseline_response_time, baseline_congestion = run_model('Baseline')

        mas_response_times.append(mas_response_time)
        mas_congestion_occurrences.append(mas_congestion)
        baseline_response_times.append(baseline_response_time)
        baseline_congestion_occurrences.append(baseline_congestion)


    print(f"Average MAS Emergency Response Time: {sum(mas_response_times) / len(mas_response_times):.2f} seconds")
    print(f"Average MAS Congestion Occurrence: {sum(mas_congestion_occurrences) / len(mas_congestion_occurrences)} times")

    print(f"Average Baseline Emergency Response Time: {sum(baseline_response_times) / len(baseline_response_times):.2f} seconds")
    print(f"Average Baseline Congestion Occurrence: {sum(baseline_congestion_occurrences) / len(baseline_congestion_occurrences)} times")

if __name__ == "__main__":
    test_traffic_model()
