% MATLAB code equivalent to the provided C# program

% Set up serial port
port = serial('COM7', 'BaudRate', 9600);
fopen(port);

% File path for writing data
path = 'D:\Data.txt';
dataFile = fopen(path, 'w');

% Threshold for voltage
threshold = 1500;

% Print date and time
dateString = datestr(now);
fprintf('Date and Time: %s\n', dateString);
fprintf(dataFile, 'Date and Time: %s\n', dateString);

% Initialize random number generator
rng('shuffle'); % Use current time as seed

fprintf('\n                 ALICE                    |                                 BOB\n');
fprintf('__________________________________________|__________________________________________________________________\n');
fprintf('                   |                          |               |     +                     |             x\n');
fprintf('       BASE        |   Polarization       |     BASE      |    D0           D1        |      D2           D3\n');
fprintf('___________________|______________________|_______________|___________________________|_________________________\n');

while true
    % Generate a random number
    randomNumber = randi([0, 7]);
    fprintf(port, '%d', randomNumber);
    
    % ALICE_BASE
    input = fscanf(port, '%s', 1);
    AliceBase = ftnBase(input);
    fprintf('        %s', AliceBase);
    fprintf(dataFile, '        %s', AliceBase);
    
    % POLARIZATION
    input = fscanf(port, '%s', 1);
    fprintf('          |        %s', input);
    fprintf(dataFile, '          |        %s', input);
    
    % BOB_BASE
    input = fscanf(port, '%s', 1);
    flag = strcmp(input, '+');
    fprintf('             |       %s', input);
    fprintf(dataFile, '             |       %s', input);
    
    % DETECTOR 1
    input = fscanf(port, '%s', 1);
    voltage = ftnVoltage(input, threshold);
    if flag
        fprintf('       |     %s', voltage);
    else
        fprintf('       |         ');
    end
    fprintf(dataFile, '       |     %s', voltage);
    
    % DETECTOR 2
    input = fscanf(port, '%s', 1);
    voltage = ftnVoltage(input, threshold);
    if flag
        fprintf('      %s', voltage);
    else
        fprintf('               ');
    end
    fprintf(dataFile, '      %s', voltage);
    
    % DETECTOR 3
    input = fscanf(port, '%s', 1);
    voltage = ftnVoltage(input, threshold);
    if ~flag
        fprintf('   |      %s', voltage);
    else
        fprintf('    |');
    end
    fprintf(dataFile, '   |      %s', voltage);
    
    % DETECTOR 4
    input = fscanf(port, '%s', 1);
    voltage = ftnVoltage(input, threshold);
    if ~flag
        fprintf('        %s\n', voltage);
    else
        fprintf('             \n');
    end
    fprintf(dataFile, '        %s\n', voltage);
    
    % Check for key press to exit the loop
    if keyAvailable()
        break;
    end
end

% Close files and port
fclose(dataFile);
fclose(port);

% Function to check for key press
function result = keyAvailable()
    result = false;
    if kbhit()
        key = getkey();
        if double(key) ~= 0
            result = true;
        end
    end
end

% Function to convert voltage to binary based on threshold
function result = ftnVoltage(value, threshold)
    temp = str2double(value);
    if temp < threshold
        temp = 0;
    else
        temp = 1;
    end
    result = num2str(temp);
end

% Function to convert base values for ALICE
function result = ftnBase(value)
    switch value
        case 'H'
            result = '+';
        case 'V'
            result = '+';
        case 'D'
            result = 'x';
        case 'A'
            result = 'x';
        otherwise
            result = '';
    end
end