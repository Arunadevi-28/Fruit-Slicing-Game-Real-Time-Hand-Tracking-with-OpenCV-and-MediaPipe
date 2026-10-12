import math
import os
import wave
import struct


OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "sounds"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)


SAMPLE_RATE = 44100


def create_tone(
    filename,
    start_frequency,
    end_frequency,
    duration,
    volume=0.4
):
    path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    total_samples = int(
        SAMPLE_RATE * duration
    )

    frames = []

    for i in range(total_samples):

        progress = i / total_samples

        frequency = (
            start_frequency
            + (end_frequency - start_frequency)
            * progress
        )

        envelope = 1.0 - progress

        value = (
            math.sin(
                2 * math.pi
                * frequency
                * i
                / SAMPLE_RATE
            )
            * volume
            * envelope
        )

        sample = int(
            value * 32767
        )

        frames.append(
            struct.pack(
                "<h",
                sample
            )
        )

    with wave.open(path, "wb") as sound:

        sound.setnchannels(1)
        sound.setsampwidth(2)
        sound.setframerate(SAMPLE_RATE)

        sound.writeframes(
            b"".join(frames)
        )

    print("Created:", path)


def create_multi_tone(
    filename,
    tones
):
    path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    frames = []

    for frequency, duration, volume in tones:

        total_samples = int(
            SAMPLE_RATE * duration
        )

        for i in range(total_samples):

            progress = i / total_samples

            envelope = 1.0 - progress

            value = (
                math.sin(
                    2 * math.pi
                    * frequency
                    * i
                    / SAMPLE_RATE
                )
                * volume
                * envelope
            )

            sample = int(
                value * 32767
            )

            frames.append(
                struct.pack(
                    "<h",
                    sample
                )
            )

    with wave.open(path, "wb") as sound:

        sound.setnchannels(1)
        sound.setsampwidth(2)
        sound.setframerate(SAMPLE_RATE)

        sound.writeframes(
            b"".join(frames)
        )

    print("Created:", path)


# Slice sound
create_tone(
    "slice.wav",
    1000,
    250,
    0.10,
    0.45
)


# Bomb sound
create_multi_tone(
    "bomb.wav",
    [
        (180, 0.12, 0.5),
        (100, 0.20, 0.5),
    ]
)


# Game over sound
create_multi_tone(
    "game_over.wav",
    [
        (500, 0.18, 0.45),
        (350, 0.18, 0.45),
        (200, 0.35, 0.45),
    ]
)


# Start sound
create_multi_tone(
    "start.wav",
    [
        (400, 0.12, 0.4),
        (600, 0.12, 0.4),
        (800, 0.18, 0.4),
    ]
)


# Timer tick
create_tone(
    "tick.wav",
    900,
    900,
    0.08,
    0.35
)


print()
print("All sound effects created successfully.")