class MP3player:
    def play_mp3(self,filename):
        print(f"Playing Mp3 file {filename}")

class WAVPlayer:
    def play_wav(self,filename):
        print(f"Playing WAV file {filename}")
        
class WAVAdapter:
    def __init__(self,wave):
        self.wave = wave

    def play(self,filename):
        self.wave.play_wav(filename) 

mp3_player = MP3player()
wav_player = WAVPlayer()
wav_adapter = WAVAdapter(wav_player)

# Client wants the same method name:
mp3_player.play_mp3("song.mp4")  # direct
wav_adapter.play("movie.wav")    # through adapter
        
