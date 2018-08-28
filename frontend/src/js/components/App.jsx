import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import EventList from "./EventList.jsx"

export default class App extends Component {
	render() {
	return (
		<>
			<Button variant="contained" color="primary">
			Hello World
			</Button>
			<Card>
				<CardContent>
				<Typography color="textSecondary">
				Word of the Day
				</Typography>
				</CardContent>
			</Card>
			<EventList/>
		</>
		);
	}
}