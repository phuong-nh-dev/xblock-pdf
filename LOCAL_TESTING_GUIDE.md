# 🧪 Local Testing Guide for xblock-pdf

## Method 1: Direct Local Installation (Recommended)

### For Tutor Development
```bash
# 1. Navigate to your xblock directory
cd /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf

# 2. Install locally in development mode
pip install -e .

# 3. Add to tutor config using local path
nano "$(tutor config printroot)/config.yml"

# Add this line (use absolute path):
OPENEDX_EXTRA_PIP_REQUIREMENTS:
  - "-e /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf"

# 4. Rebuild and start
tutor config save
tutor images build openedx
tutor local start -d
```

### For Native OpenEDX Installation
```bash
# 1. Install in edxapp environment
sudo -u edxapp /edx/bin/pip.edxapp install -e /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf

# 2. Restart services
sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:
```

## Method 2: XBlock Workbench (Quick Testing)

### Install XBlock SDK
```bash
# Create virtual environment
python3 -m venv xblock-env
source xblock-env/bin/activate

# Install XBlock SDK
pip install xblock-sdk

# Install your xblock
cd /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf
pip install -e .
```

### Run Workbench
```bash
# Start the workbench server
xblock-sdk runserver

# Open browser to: http://localhost:8000
# Your PDF XBlock will be available for testing
```

## Method 3: Docker Development Environment

### Create Dockerfile for Testing
```dockerfile
FROM python:3.9

# Install dependencies
RUN pip install xblock-sdk

# Copy your xblock
COPY . /app/xblock-pdf
WORKDIR /app/xblock-pdf

# Install in development mode
RUN pip install -e .

# Expose port
EXPOSE 8000

# Run workbench
CMD ["xblock-sdk", "runserver", "0.0.0.0:8000"]
```

### Build and Run
```bash
# Build container
docker build -t xblock-pdf-test .

# Run container
docker run -p 8000:8000 xblock-pdf-test

# Access at http://localhost:8000
```

## Method 4: Unit Testing (Fastest)

### Run Python Tests
```bash
cd /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf

# Install test dependencies
pip install pytest pytest-django mock

# Run tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_teak_compatibility.py -v

# Run with coverage
python -m pytest tests/ --cov=pdf --cov-report=html
```

### Run JavaScript Tests
```bash
# Install Node dependencies
npm install

# Run linting
npm run lint

# Run Grunt tests
npm test
```

## Method 5: Manual Validation

### Validate Setup
```bash
cd /Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf

# Check setup.py
python3 setup.py check --strict

# Validate compatibility
python3 validate_teak_compatibility.py

# Test import
python3 -c "from pdf.pdf import PdfBlock; print('Import successful!')"
```

## Method 6: Tutor Development Mode

### Enable Development Mode
```bash
# Mount local directory in tutor
tutor config save --set OPENEDX_EXTRA_PIP_REQUIREMENTS='["-e /path/to/your/xblock-pdf"]'

# Use tutor dev mode for faster iteration
tutor dev start

# Your changes will be reflected immediately
```

## Quick Test Scenarios

### Test 1: Basic Functionality
1. Create a course
2. Add Advanced -> PDF component
3. Configure with test PDF URL
4. Verify display and download work

### Test 2: Studio Editing
1. Edit the PDF component in Studio
2. Change display name, URL, download settings
3. Save and verify changes persist

### Test 3: Event Tracking
1. Check browser developer tools
2. Monitor network requests when:
   - Loading PDF
   - Downloading PDF
3. Verify tracking events are sent

## Troubleshooting

### Common Issues
```bash
# If import fails
export PYTHONPATH="/Users/phuongnguyen/Documents/work/steam-open-edx/xblock-pdf:$PYTHONPATH"

# If Django not found
pip install Django>=4.2

# If XBlock not found  
pip install XBlock>=2.0.0

# Clear Python cache
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
```

### Debug Mode
```python
# Add to pdf/pdf.py for debugging
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.debug("PDF XBlock loaded successfully")
```

## Recommended Testing Flow

1. **Start with Unit Tests** (`pytest tests/`)
2. **Validate Compatibility** (`python3 validate_teak_compatibility.py`)  
3. **Test with Workbench** (`xblock-sdk runserver`)
4. **Test in Tutor Dev Mode** (if using Tutor)
5. **Manual Testing** in full OpenEDX environment

This approach ensures your XBlock works perfectly before any GitHub deployment! 🚀
