import time
import random
import os
import pygame

# --- CONFIGURATION ---
# Name of your audio file (WAV or MP3)
AUDIO_FILENAME = "test_track.mp3" 

# How many seconds of the song to play?
PLAY_DURATION = 15 

# How many total trials?
TOTAL_TRIALS = 10

# The names of your devices
DEVICE_A = "JDS Labs"
DEVICE_B = "Scarlett Solo"

# ---------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_audio_segment():
    print(f"\n🎵 Playing {PLAY_DURATION} seconds of audio...")
    pygame.mixer.music.load(AUDIO_FILENAME)
    pygame.mixer.music.play()
    
    # Wait for the duration
    time.sleep(PLAY_DURATION)
    
    pygame.mixer.music.stop()
    print("⏹️ Audio stopped.")

def countdown(seconds, message):
    print(f"\n{message}")
    for i in range(seconds, 0, -1):
        print(f" {i}...", end='\r', flush=True)
        time.sleep(1)
    print(" 0 - GO!          ")

def main():
    # Initialize Audio
    pygame.mixer.init()
    
    # Verify file exists
    if not os.path.exists(AUDIO_FILENAME):
        print(f"ERROR: Could not find '{AUDIO_FILENAME}' in this folder.")
        return

    # Generate the randomized sequence
    # We ensure a balanced mix, then shuffle
    half_trials = TOTAL_TRIALS // 2
    sequence = [DEVICE_A] * half_trials + [DEVICE_B] * (TOTAL_TRIALS - half_trials)
    random.shuffle(sequence)

    results = []

    clear_screen()
    print("### BLIND A/B TEST AUTOMATION ###")
    print("Instructions for the OPERATOR (Brother):")
    print("1. Follow the on-screen prompts exactly.")
    print("2. When prompted to 'Unplug', physically unplug the headphones.")
    print("3. When prompted to 'Connect', plug into the requested device.")
    print("4. The script will handle the 5-second waiting period.")
    print("\nPress ENTER to begin the test...")
    input()

    for i, target_device in enumerate(sequence, 1):
        clear_screen()
        print(f"--- TRIAL {i} of {TOTAL_TRIALS} ---")
        print("\n(Listener: Please close your eyes or look away)")
        
        # 1. The Disconnect Phase
        print("\n⚠️  ACTION: UNPLUG HEADPHONES NOW.")
        input(">> Press ENTER when unplugged...")

        # 2. The Delay/Switch Phase (The Fake-out window)
        # We enforce a delay so the listener can't judge by speed
        countdown(5, "⏳ SWAPPING CABLES (Make noise, move cables around)...")

        # 3. The Connect Phase
        print(f"\n👉 ACTION: CONNECT TO [{target_device}]")
        print("   (Do not say anything out loud)")
        input(">> Press ENTER when connected...")

        # 4. The Listen Phase
        play_audio_segment()

        # 5. Logging Phase
        print("\nListener: Write down your guess now.")
        input(">> Press ENTER to move to next trial...")
        
        # Save to list
        results.append(f"Trial {i}: {target_device}")

    # End of test
    clear_screen()
    print("Test Complete!")
    
    # Save results to file
    with open("answer_key.txt", "w") as f:
        f.write("OFFICIAL ANSWER KEY\n===================\n")
        for line in results:
            f.write(line + "\n")
    
    print("\nAn 'answer_key.txt' file has been created in this folder.")
    print("Open it to compare with the listener's written notes.")

if __name__ == "__main__":
    main()
