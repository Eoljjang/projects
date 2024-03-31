const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  devtool: 'inline-source-map', // Make it easier to track where error messages come from.
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },

  plugins: [
    new HtmlWebpackPlugin({
        // Puts the entire src/index.html output into dist/index.html
        template: './src/index.html'
    }),
  ],

  module:{
    rules:[
        { // 1) Link css files.
            test: /\.css$/i,
            use: ['style-loader', 'css-loader'],
        },
        { // 2) link any assets.
            test:/\.(png|svg|jpg|jpeg|gif)%/i,
            type: 'asset/resource',
        }
    ]
    }
};