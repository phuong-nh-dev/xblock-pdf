module.exports = {
    env: {
        browser: true,
        jquery: true,
        es6: false
    },
    extends: [
        'eslint:recommended'
    ],
    globals: {
        // XBlock runtime globals
        runtime: 'readonly',
        element: 'readonly'
    },
    parserOptions: {
        ecmaVersion: 5,
        sourceType: 'script'
    },
    rules: {
        'indent': ['error', 4],
        'linebreak-style': ['error', 'unix'],
        'quotes': ['error', 'single'],
        'semi': ['error', 'always'],
        'no-unused-vars': ['warn'],
        'no-console': ['warn']
    }
};
