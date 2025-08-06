#!/bin/bash
echo "🔍 Watching sort.py for changes..."
echo "Press Ctrl+C to stop"

# Kill any existing python processes for this script
pkill -f "python.*sort.py" 2>/dev/null

# Function to run the script
run_script() {
    echo "🔄 Running sort.py..."
    python sort.py &
    SCRIPT_PID=$!
}

# Initial run
run_script

# Watch for file changes
fswatch -o sort.py | while read f; do
    echo "📝 File changed, restarting..."
    kill $SCRIPT_PID 2>/dev/null
    sleep 0.5
    run_script
done