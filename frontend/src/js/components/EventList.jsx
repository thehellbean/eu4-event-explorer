import React, { Component } from 'react';
import { connect } from 'react-redux';
import { eventsFetchData } from '../actions/items';
import Event from './Event.jsx'

const mapStateToProps = (state) => {
	return {
		events: state.events,
		hasErrored: state.eventsHasErrored,
		isLoading: state.eventsIsLoading
	};
};

const mapDispatchToProps = (dispatch) => {
	return {
		fetchData: (url, parameters) => dispatch(eventsFetchData(url, parameters))
	};
}

class EventList extends Component {
	render() {
		if (this.props.hasErrored) {
			return <p>Sorry! There was an error loading the items</p>;
		}

		if (this.props.isLoading) {
			return <p>Loading...</p>;
		}

		return (
			<ul>
				{this.props.events.map((item) => (
						<Event key={item.id} event={item}/>				
					))
				}
			</ul>
		);
	}
}

export default connect(mapStateToProps, mapDispatchToProps)(EventList);