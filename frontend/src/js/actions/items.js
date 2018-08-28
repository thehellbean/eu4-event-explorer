import { EVENTS_HAS_ERRORED, EVENTS_IS_LOADING, EVENTS_FETCH_DATA_SUCCESS } from "../constants/action-types";

export function eventsHasErrored(bool) {
	return {
		type: EVENTS_HAS_ERRORED,
		hasErrored: bool
	};
}

export function eventsIsLoading(bool) {
	return {
		type: EVENTS_IS_LOADING,
		isLoading: bool
	}
}

export function eventsFetchDataSuccess(events) {
	return {
		type: EVENTS_FETCH_DATA_SUCCESS,
		events
	}
}

export function eventsFetchData(url, parameters) {
	return (dispatch) => {
		dispatch(itemIsLoading(true));

		fetch(url)
			.then((response) => {
				if (!response.ok) {
					throw Error(response.statusText);
				}

				dispatch(itemIsLoading(false));

				return response;
			})
			.then((response) => response.json())
			.then((events) => 
				dispatch(eventsFetchDataSuccess(events)))
			.catch(() => dispatch(eventsHasErrored(true)));
	}
}