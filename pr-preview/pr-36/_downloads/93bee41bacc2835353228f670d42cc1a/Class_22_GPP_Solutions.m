%% Class 22: GPP - SOLUTION KEY
%
% Instructions: Complete the following problems by writing your code
% in the indicated sections. Test each section before moving on.


%% =========================================================================
%% PROBLEM 1: Signal Processing - Finding Peaks in Noisy Data (12 minutes)
%% =========================================================================
% A sensor records temperature fluctuations over time. Your goal is to
% identify significant temperature spikes.

% Given data (copy and run this):
time = 0:0.1:10;  % Time in seconds
temperature = 20 + 5*sin(2*pi*0.5*time) + randn(size(time));  % Temperature in Celsius

% Part A (3 pts): Plot the temperature data vs. time
% Add appropriate labels and title

% SOLUTION:
figure;
plot(time, temperature);
xlabel('Time (s)');
ylabel('Temperature (°C)');
title('Temperature Sensor Data');
grid on;


% Part B (4 pts): Use findpeaks() to find ALL peaks in the temperature data
% (A peak is any local maximum - a point higher than its immediate neighbors)
% Store the peak values in a variable called 'peaks'
% Store the peak locations in a variable called 'locations'
% Display how many peaks were found using fprintf

% SOLUTION:
[peaks, locations] = findpeaks(temperature);
fprintf('Number of peaks found: %d\n', length(peaks));


% Part C (5 pts): Now find only SIGNIFICANT peaks using these criteria:
%   - Minimum peak height: 23°C
%   - Minimum distance between peaks: 10 samples
% Plot the original data AND mark the significant peaks with red circles
% Display how many significant peaks were found
% (HINT: use hold on and plot time(locations), peaks, 'ro')

% SOLUTION:
[peaks, locations] = findpeaks(temperature, 'MinPeakHeight', 23, 'MinPeakDistance', 10);
fprintf('Number of significant peaks found: %d\n', length(peaks));

figure;
plot(time, temperature);
hold on;
plot(time(locations), peaks, 'ro', 'MarkerSize', 8, 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Temperature (°C)');
title('Temperature Data with Significant Peaks Marked');
legend('Temperature', 'Significant Peaks');
grid on;
hold off;


%% =========================================================================
%% PROBLEM 2: Statistics - Analyzing Heart Rate Data (15 minutes)
%% =========================================================================
% You collected heart rate data from 20 subjects under two conditions:
% resting and after exercise.

% Given data (copy and run this):
restingHR = [72, 68, 75, 70, 73, 69, 71, 74, 68, 72, 70, 73, 71, 69, 72, 74, 70, 68, 71, 73];
exerciseHR = [145, 138, 152, 141, 148, 136, 143, 150, 139, 145, 142, 147, 144, 137, 146, 151, 140, 138, 143, 148];

% Part A (3 pts): Create a histogram of the resting heart rate data
% Include appropriate axis labels and title

% SOLUTION:
figure;
histogram(restingHR);
xlabel('Heart Rate (bpm)');
ylabel('Frequency');
title('Distribution of Resting Heart Rate');
grid on;


% Part B (4 pts): Calculate and display the following statistics for BOTH conditions:
%   - Mean
%   - Median
%   - Standard deviation
% Format: "Resting - Mean: XX.X, Median: XX.X, Std: XX.X"

% SOLUTION:
restingMean = mean(restingHR);
restingMedian = median(restingHR);
restingStd = std(restingHR);

exerciseMean = mean(exerciseHR);
exerciseMedian = median(exerciseHR);
exerciseStd = std(exerciseHR);

fprintf('Resting - Mean: %.1f, Median: %.1f, Std: %.1f\n', ...
    restingMean, restingMedian, restingStd);
fprintf('Exercise - Mean: %.1f, Median: %.1f, Std: %.1f\n', ...
    exerciseMean, exerciseMedian, exerciseStd);


% Part C (5 pts): Create a box plot to compare the two conditions
% HINT: You need to combine the data and create group labels
%   combinedData = [restingHR, exerciseHR]';
%   groups = [ones(1,20), 2*ones(1,20)]';
% Label the x-axis categories as 'Resting' and 'Exercise'
% Add appropriate y-axis label and title

% SOLUTION:
combinedData = [restingHR, exerciseHR]';
groups = [ones(1,20), 2*ones(1,20)]';

figure;
boxchart(groups, combinedData);
xticklabels({'Resting', 'Exercise'});
ylabel('Heart Rate (bpm)');
title('Comparison of Resting vs. Exercise Heart Rate');
grid on;


% Part D (3 pts): Perform a two-sample t-test to determine if the heart rates
% are significantly different between conditions
% Display a message: "Heart rates are significantly different" or
%                   "No significant difference detected"

% SOLUTION:
h = ttest2(restingHR, exerciseHR);

if h == 1
    disp('Heart rates are significantly different');
else
    disp('No significant difference detected');
end


%% =========================================================================
%% PROBLEM 3: Signal Processing - ECG Peak Detection (12 minutes)
%% =========================================================================
% This problem simulates what you'll do in your course project.
% You have a simplified ECG signal and need to detect heartbeats.

% Given data (copy and run this):
t = 0:0.001:5;  % 5 seconds of data
ecg = sin(2*pi*1.2*t) + 0.3*sin(2*pi*2.4*t) + 0.2*randn(size(t));  % Simulated ECG

% Part A (4 pts): Plot the ECG signal
% Label axes as 'Time (s)' and 'Voltage (mV)'

% SOLUTION:
figure;
plot(t, ecg);
xlabel('Time (s)');
ylabel('Voltage (mV)');
title('Simulated ECG Signal');
grid on;


% Part B (5 pts): Use findpeaks() to detect R-peaks (heartbeats) with these criteria:
%   - Minimum peak height: 0.5 mV
%   - Minimum peak distance: 400 samples (to avoid detecting the same beat twice)
% Store results in variables: peakVoltages and peakLocations

% SOLUTION:
[peakVoltages, peakLocations] = findpeaks(ecg, 'MinPeakHeight', 0.5, 'MinPeakDistance', 400);

% Optional: Plot ECG with detected peaks marked
figure;
plot(t, ecg);
hold on;
plot(t(peakLocations), peakVoltages, 'ro', 'MarkerSize', 8, 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Voltage (mV)');
title('ECG Signal with Detected R-Peaks');
legend('ECG Signal', 'R-Peaks');
grid on;
hold off;


% Part C (3 pts): Calculate and display the heart rate in beats per minute (bpm)
% HINT: Count the number of peaks, divide by total time in minutes
%       Heart rate = (number of peaks / total time in minutes)

% SOLUTION:
numBeats = length(peakVoltages);
totalTimeMinutes = max(t) / 60;
heartRate = numBeats / totalTimeMinutes;

fprintf('Heart rate: %.1f bpm\n', heartRate);


%% =========================================================================
%% PROBLEM 4: Optimization - Minimizing a Cost Function (11 minutes)
%% =========================================================================
% A company's profit function is: P(x) = -2x^2 + 20x - 30
% where x is the number of units produced (in thousands)

% Part A (3 pts): Create an anonymous function for the COST (negative profit)
% Name it: costFunction
% HINT: To minimize profit, we maximize cost, so cost = -P(x) = 2x^2 - 20x + 30

% SOLUTION:
costFunction = @(x) 2*x^2 - 20*x + 30;


% Part B (5 pts): Use fminunc() to find the optimal production level
% - Start with an initial guess of x0 = 0
% - Store the optimal x value in: optimalProduction
% - Store the minimum cost in: minCost
% HINT: [optimalProduction, minCost] = fminunc(costFunction, x0);

% SOLUTION:
x0 = 0;
options = optimoptions('fminunc', 'Display', 'off');  % Turn off iteration display
[optimalProduction, minCost] = fminunc(costFunction, x0, options);


% Part C (3 pts): Calculate the maximum profit and display results
% Format: "Optimal production: X.XX thousand units"
%         "Maximum profit: $X.XX"

% SOLUTION:
maxProfit = -minCost;  % Since cost = -profit

fprintf('Optimal production: %.2f thousand units\n', optimalProduction);
fprintf('Maximum profit: $%.2f\n', maxProfit);


%% =========================================================================
%% BONUS CHALLENGE: Combining Multiple Toolboxes (Optional - if time permits)
%% =========================================================================
% Create synthetic ECG data, add noise, detect peaks, and perform statistical analysis

% Part A: Generate a synthetic ECG signal (3 minutes)
% - Time vector: 0 to 10 seconds, 1000 samples per second
% - Signal: 1.5*sin(2*pi*1.5*t) with added noise (0.3*randn)

% SOLUTION:
samplingRate = 1000;  % Hz
t_bonus = 0:1/samplingRate:10;  % 0 to 10 seconds
ecg_bonus = 1.5*sin(2*pi*1.5*t_bonus) + 0.3*randn(size(t_bonus));

figure;
plot(t_bonus, ecg_bonus);
xlabel('Time (s)');
ylabel('Voltage (mV)');
title('Synthetic ECG Signal');
grid on;


% Part B: Detect peaks and calculate inter-beat intervals (4 minutes)
% - Use findpeaks with appropriate parameters
% - Calculate time between consecutive beats (RR intervals)
% HINT: diff(peakLocations) gives you the intervals in samples
%       Convert to seconds by dividing by sampling rate

% SOLUTION:
[pks_bonus, locs_bonus] = findpeaks(ecg_bonus, 'MinPeakHeight', 1.0, ...
    'MinPeakDistance', 400);

% Calculate RR intervals
rrIntervalsSamples = diff(locs_bonus);
rrIntervalsSeconds = rrIntervalsSamples / samplingRate;

fprintf('Number of heartbeats detected: %d\n', length(pks_bonus));
fprintf('Mean RR interval: %.3f seconds\n', mean(rrIntervalsSeconds));


% Part C: Statistical analysis of heart rate variability (3 minutes)
% - Calculate mean and standard deviation of RR intervals
% - Create a histogram of RR intervals

% SOLUTION:
meanRR = mean(rrIntervalsSeconds);
stdRR = std(rrIntervalsSeconds);

fprintf('RR Interval Statistics:\n');
fprintf('  Mean: %.3f s\n', meanRR);
fprintf('  Std Dev: %.3f s\n', stdRR);

figure;
histogram(rrIntervalsSeconds);
xlabel('RR Interval (s)');
ylabel('Frequency');
title('Distribution of RR Intervals (Heart Rate Variability)');
grid on;

% Calculate average heart rate from RR intervals
avgHeartRate = 60 / meanRR;  % Convert from seconds to bpm
fprintf('Average heart rate: %.1f bpm\n', avgHeartRate);



