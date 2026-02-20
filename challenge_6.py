song_time = input("Enter song durations: ")
values = song_time.split()

playlist = []

for value in values:
    playlist.append(int(value))

invalid = False
for duration in playlist:
    if duration <= 0:
        invalid = True
        break

if invalid:
    print("Invalid Playlist: Contains non-positive durations")
else:
    total_duration = sum(playlist)
    number_of_songs = len(playlist)

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", number_of_songs)

    if total_duration < 300:
        print("Category: Too Short Playlist")
        print("Recommendation: Add more songs")

    elif total_duration > 3600:
        print("Category: Too Long Playlist")
        print("Recommendation: Consider splitting the playlist")

    else:
        repetitive = False
        for duration in playlist:
            if playlist.count(duration) > 1:
                repetitive = True
                break

        if repetitive:
            print("Category: Repetitive Playlist")
            print("Recommendation: Add variety")
        else:
            variation = max(playlist) - min(playlist)

            if variation >= 30:
                print("Category: Balanced Playlist")
                print("Recommendation: Good listening session")
            else:
                print("Category: Irregular Playlist")
                print("Recommendation: Adjust song durations for better balance")
