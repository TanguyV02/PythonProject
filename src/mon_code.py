import numpy as np
import matplotlib.pyplot as plt

# Function to generate a simple sine wave signal
def generate_signal(freq=5, sampling_rate=100, duration=1):
    """
    Generate a sine wave signal.

    Parameters:
    freq (float): Frequency of the sine wave in Hz.
    sampling_rate (int): Number of samples per second.
    duration (float): Duration of the signal in seconds.

    Returns:
    tuple: Time vector (t) and the generated sine wave (signal).
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time vector
    signal = np.sin(2 * np.pi * freq * t)  # Sine wave signal
    return t, signal

# Function to add noise to a signal
def add_noise(signal, noise_level=0.2):
    """
    Add random noise to a signal.

    Parameters:
    signal (array): Input signal.
    noise_level (float): Standard deviation of the Gaussian noise.

    Returns:
    array: Noisy signal.
    """
    noise = np.random.normal(0, noise_level, len(signal))  # Generate noise
    noisy_signal = signal + noise
    return noisy_signal

# Function to compute the Fourier Transform of a signal
def compute_fourier_transform(signal, sampling_rate):
    """
    Compute the Fast Fourier Transform (FFT) of a signal.

    Parameters:
    signal (array): Input signal.
    sampling_rate (int): Sampling rate of the signal in Hz.

    Returns:
    tuple: Frequencies and their corresponding magnitudes.
    """
    fft_result = np.fft.fft(signal)  # Compute FFT
    fft_magnitude = np.abs(fft_result)  # Get magnitude
    fft_freq = np.fft.fftfreq(len(signal), d=1/sampling_rate)  # Frequency bins
    return fft_freq, fft_magnitude

# Function to plot the signal and its Fourier Transform
def plot_results(t, signal, fft_freq, fft_magnitude):
    """
    Plot the original signal and its Fourier Transform.

    Parameters:
    t (array): Time vector.
    signal (array): Original signal.
    fft_freq (array): Frequency bins from FFT.
    fft_magnitude (array): Magnitude of FFT.
    """
    plt.figure(figsize=(12, 6))

    # Plot the time-domain signal
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title("Time-Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Plot the frequency-domain signal
    plt.subplot(2, 1, 2)
    plt.plot(fft_freq[:len(fft_freq)//2], fft_magnitude[:len(fft_magnitude)//2])  # Only positive frequencies
    plt.title("Frequency-Domain Signal (Fourier Transform)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.show()

# Main function to demonstrate the Fourier Transform process
def main():
    """
    Main function to demonstrate the generation of a signal, addition of noise,
    computation of the Fourier Transform, and plotting the results.
    """
    # Step 1: Generate a clean sine wave
    freq = 5  # Frequency in Hz
    sampling_rate = 100  # Samples per second
    duration = 2  # Signal duration in seconds
    t, clean_signal = generate_signal(freq, sampling_rate, duration)

    # Step 2: Add noise to the signal
    noisy_signal = add_noise(clean_signal, noise_level=0.3)

    # Step 3: Compute the Fourier Transform
    fft_freq, fft_magnitude = compute_fourier_transform(noisy_signal, sampling_rate)

    # Step 4: Plot the results
    plot_results(t, noisy_signal, fft_freq, fft_magnitude)

# Run the main function
if __name__ == "__main__":
    main()
