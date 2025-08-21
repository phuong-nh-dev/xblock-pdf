# xblock-pdf v2.0 - OpenEDX Teak Compatible

[![Build Status](https://circleci.com/gh/IONISx/xblock-pdf.svg?style=svg)](https://circleci.com/gh/IONISx/xblock-pdf)

> Course component (Open edX XBlock) that provides an easy way to embed a PDF - **Updated for OpenEDX Teak Release Compatibility**

## Features

- Download button available
- (Optional) Source document download button, for example to provide your PPT file
- Create tracking logs:
  - `edx.pdf.loaded` when a student loads the PDF
  - `edx.pdf.downloaded` when a student downloads the PDF

## Customize the XBlock

By default, PDF Download Allowed is set to `True`.
The default value can be changed in `xblock-pdf/pdf/ pdf.py`

## What's New in v2.0

- ✅ **OpenEDX Teak Release Compatible**
- ✅ **Modern Python 3.8+ Support**
- ✅ **Updated XBlock Dependencies**
- ✅ **Improved Error Handling**
- ✅ **Modern Development Tools**
- ✅ **Better Template Rendering**
- ✅ **Enhanced Studio Integration**

## Install / Update the XBlock

### For Tutor EDX (Recommended)

Add it to config.yml using this parameter:

```bash
nano "$(tutor config printroot)/config.yml"
```

```yml
OPENEDX_EXTRA_PIP_REQUIREMENTS:
  - "git+https://github.com/your-repo/xblock-pdf.git@v2.0.0#egg=xblock-pdf"
```

Save your config file and rebuild:

```bash
tutor config save
tutor images build openedx
tutor local start -d
```

### For Native OpenEDX Installation

Add it to the `EDXAPP_EXTRA_REQUIREMENTS` variable:

```yml
EDXAPP_EXTRA_REQUIREMENTS:
  - name: "git+https://github.com/your-repo/xblock-pdf.git@v2.0.0#egg=xblock-pdf"
```

Then run your deployment playbooks.

### Restart your Open edX processes

```shell
sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:
```

Not needed in tutor EDX

# Use the XBlock

### Activate the XBlock in your course

Go to `Settings -> Advanced Settings` and set `advanced_modules` to `["pdf"]`.

### Use the XBlock in a unit

Select `Advanced -> PDF` in your unit.

## Development Environment

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm 8+

### Setup

1. **Install JavaScript dependencies:**

   ```bash
   npm install -g grunt-cli
   npm install
   ```

2. **Install Python dependencies (preferably in a virtualenv):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Development Commands

- **Run linting:** `grunt test`
- **Build assets:** `npm run build` or `grunt build`
- **Lint code:** `npm run lint`
- **Format code:** `npm run format`
- **Watch for changes:** `grunt dev`

## License

GNU Affero General Public License 3.0 (AGPL 3.0)
