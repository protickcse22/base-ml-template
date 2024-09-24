# 1. Echo start of the script
echo [$(date)] "Starting the script..."

# 2. Create a conda environment
conda create -p .venv python=3.12 -y
echo "Activating conda environment and installing dependencies..."
source activate .venv

pip install -r requirements_dev.txt
echo "Script completed successfully!"