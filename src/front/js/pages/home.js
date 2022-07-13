import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";

import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	const [imagenSelect, setImagenSelect] = useState("");
	const [loadin, setLoading] = useState(false);

	const subirImagen = async (foto) => {
		console.log(foto);
		const data = new FormData();
		data.append("file", foto);
		data.append("upload_preset", "usuarios-liberte");
		setLoading(true);
		const resp = await fetch(
			"https://api.cloudinary.com/v1_1/yisusrobles/image/upload",
			{
				method: "POST",
				// mode: "no-cors",
				body: data,
			}
		);
		const file = await resp.json();
		console.log(file);
		setImagenSelect(file.secure_url);
		setLoading(false);


	};

	const enviarInfo = async () => {

		const resp = await fetch("https://3001-gray-gecko-82vrjdj4fol.ws-eu54.gitpod.io/api/upload", {
			method: "POST",
			mode: "no-cors",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				foto: imagenSelect
			}),
		})
		// const data = await resp.json();
		// console.log("data", data)
	};

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<input
				type="file"
				name="pic"
				onChange={(e) => {
					subirImagen(e.target.files[0]);
				}}
			></input>
			<button onClick={enviarInfo}></button>
			<input type="submit" onClick={enviarInfo} />
		</div>
	);
};

// const request = async (url) => {
// 	const response = await fetch(url);
// 	if (!response.ok)
// 		throw new Error("WARN", response.status);
// 	const data = await response.text();
// 	return data;
// }

// const resultOk = await request("/robots.txt");
// const resultError = await request("/nonExistentFile.txt");
