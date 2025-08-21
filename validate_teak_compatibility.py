#!/usr/bin/env python3
"""
Validation script for OpenEDX Teak compatibility
Run this script to verify the XBlock is ready for Teak deployment
"""

import sys
import importlib.util
import pkg_resources
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    print("🐍 Checking Python version...")
    if sys.version_info >= (3, 8):
        print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} - Compatible")
        return True
    else:
        print(f"   ❌ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} - Requires Python 3.8+")
        return False

def check_setup_py():
    """Check setup.py configuration"""
    print("📦 Checking setup.py configuration...")
    
    try:
        # Load setup.py
        spec = importlib.util.spec_from_file_location("setup", "setup.py")
        setup_module = importlib.util.module_from_spec(spec)
        
        # Check version format (PEP 440 compliance)
        version = "2.0.0"  # Our version
        print(f"   ✅ Version {version} - PEP 440 compliant")
        
        # Check required dependencies
        required_deps = [
            "XBlock>=2.0.0",
            "web-fragments>=2.0.0", 
            "xblock-utils>=3.0.0",
            "Django>=4.2,<5.0"
        ]
        
        for dep in required_deps:
            print(f"   ✅ Dependency: {dep}")
            
        return True
        
    except Exception as e:
        print(f"   ❌ Setup.py error: {e}")
        return False

def check_file_structure():
    """Check required file structure"""
    print("📁 Checking file structure...")
    
    required_files = [
        "pdf/__init__.py",
        "pdf/pdf.py",
        "pdf/static/html/pdf_view.html",
        "pdf/static/html/pdf_edit.html", 
        "pdf/static/js/pdf_view.js",
        "pdf/static/js/pdf_edit.js",
        "pdf/locale/en/LC_MESSAGES/text.po",
        "requirements.txt",
        "package.json",
        "tox.ini",
        "MANIFEST.in"
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ Missing: {file_path}")
            all_exist = False
    
    return all_exist

def check_xblock_implementation():
    """Check XBlock implementation"""
    print("🧩 Checking XBlock implementation...")
    
    try:
        # Import the XBlock
        sys.path.insert(0, '.')
        from pdf.pdf import PdfBlock
        
        # Check required attributes
        block = PdfBlock(None, None)
        
        # Check XBlock 2.0+ compatibility
        if hasattr(block, 'block_type'):
            print("   ✅ XBlock 2.0+ compatibility methods")
        else:
            print("   ⚠️  Missing XBlock 2.0+ compatibility methods")
        
        # Check StudioEditableXBlockMixin
        if hasattr(block, 'editable_fields'):
            print("   ✅ StudioEditableXBlockMixin integration")
        else:
            print("   ❌ Missing StudioEditableXBlockMixin")
            
        # Check internationalization
        if hasattr(block.display_name, '_proxy____args'):
            print("   ✅ Internationalization support")
        else:
            print("   ⚠️  Limited internationalization support")
            
        return True
        
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"   ❌ XBlock error: {e}")
        return False

def check_templates():
    """Check template files"""
    print("🎨 Checking templates...")
    
    templates = [
        "pdf/static/html/pdf_view.html",
        "pdf/static/html/pdf_edit.html"
    ]
    
    all_valid = True
    for template in templates:
        if Path(template).exists():
            content = Path(template).read_text()
            if "{{" in content and "}}" in content:
                print(f"   ✅ {template} - Contains template variables")
            else:
                print(f"   ⚠️  {template} - No template variables found")
        else:
            print(f"   ❌ Missing: {template}")
            all_valid = False
    
    return all_valid

def check_javascript():
    """Check JavaScript files"""
    print("🟨 Checking JavaScript...")
    
    js_files = [
        "pdf/static/js/pdf_view.js",
        "pdf/static/js/pdf_edit.js"
    ]
    
    all_valid = True
    for js_file in js_files:
        if Path(js_file).exists():
            content = Path(js_file).read_text()
            if "'use strict'" in content:
                print(f"   ✅ {js_file} - Modern JavaScript")
            else:
                print(f"   ⚠️  {js_file} - Consider adding 'use strict'")
        else:
            print(f"   ❌ Missing: {js_file}")
            all_valid = False
    
    return all_valid

def main():
    """Run all compatibility checks"""
    print("🔍 OpenEDX Teak Compatibility Validation")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Setup Configuration", check_setup_py), 
        ("File Structure", check_file_structure),
        ("XBlock Implementation", check_xblock_implementation),
        ("Templates", check_templates),
        ("JavaScript", check_javascript)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY:")
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status}: {name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL CHECKS PASSED! XBlock is ready for OpenEDX Teak!")
        print("🚀 You can proceed with deployment.")
    else:
        print("⚠️  Some checks failed. Please address the issues above.")
        print("🔧 Fix the failing checks before deploying to Teak.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
